#!/usr/bin/env bash
# ==============================================================================
# Riseup Help - Translation Status Checker
#
# Finds translated files that are older than the latest change to the English
# original, as well as English pages that have not yet been translated.
#
# Portable across Linux, macOS (BSD), and other Unix-like systems.
# ==============================================================================

set -e

if [ ! -d "pages" ]; then
  echo "Error: 'pages' directory not found. Please run this script from the repository root."
  exit 1
fi

SUPPORTED_LANGS="zh es pt ru de fr it el ca hi pl da lt"

usage() {
  cat << EOF
Usage: $0 [OPTIONS] <language-code>
       $0 --all

Options:
  --diff              Show git diff of the English changes since last translation
  --difftool          Open git difftool for each outdated file (interactive)
  --outdated-only     Only list translated files that are outdated
  --untranslated-only Only list files missing a translation
  --all               Show a summary table for all supported languages
  -h, --help          Show this help message

Languages:
  zh : Simplified Chinese      fr : French
  es : Spanish                 it : Italian
  pt : Portuguese              el : Greek
  ru : Russian                 ca : Catalan
  de : German                  hi : Hindi
  pl : Polish                  da : Danish
  lt : Lithuanian
EOF
  exit 0
}

MODE="summary"
LANG_ARG=""
SHOW_ALL=0

while [ "$#" -gt 0 ]; do
  case "$1" in
    -h|--help)
      usage
      ;;
    --all)
      SHOW_ALL=1
      shift
      ;;
    --diff)
      MODE="diff"
      shift
      ;;
    --difftool)
      MODE="difftool"
      shift
      ;;
    --outdated-only)
      MODE="outdated"
      shift
      ;;
    --untranslated-only)
      MODE="untranslated"
      shift
      ;;
    -*)
      echo "Unknown option: $1"
      usage
      ;;
    *)
      LANG_ARG="$1"
      shift
      ;;
  esac
done

# High-level overview of all languages
if [ "$SHOW_ALL" -eq 1 ]; then
  echo "=========================================================="
  echo "   Riseup Help Translation Overview across All Locales    "
  echo "=========================================================="
  total_en=$(find pages -type f \( -name "*.en.text" -o -name "*.en.md" -o -name "en.text" -o -name "en.md" \) | wc -l | tr -d ' ')
  echo "Total English pages: $total_en"
  echo ""
  printf "%-6s %-12s %-12s %-12s\n" "Lang" "Translated" "Outdated" "Missing"
  echo "----------------------------------------------------------"
  for l in $SUPPORTED_LANGS; do
    trans_files=$(find pages -type f \( -name "*.$l.text" -o -name "*.$l.md" -o -name "$l.text" -o -name "$l.md" \) 2>/dev/null)
    trans_count=$(echo "$trans_files" | grep -v '^$' | wc -l | tr -d ' ')
    
    outdated_count=0
    for f in $trans_files; do
      [ -z "$f" ] && continue
      orig_file=$(dirname "$f")/$(basename "$f" | sed -e "s/\.$l\./.en./" -e "s/^$l\./en./")
      if [ -f "$orig_file" ]; then
        d_trans=$(git log -n 1 --format=%ct -- "$f" 2>/dev/null || echo 0)
        d_orig=$(git log -n 1 --format=%ct -- "$orig_file" 2>/dev/null || echo 0)
        if [ "$d_orig" -gt "$d_trans" ]; then
          outdated_count=$((outdated_count + 1))
        fi
      fi
    done
    missing_count=$((total_en - trans_count))
    if [ "$missing_count" -lt 0 ]; then missing_count=0; fi
    printf "%-6s %-12s %-12s %-12s\n" "$l" "$trans_count" "$outdated_count" "$missing_count"
  done
  echo "=========================================================="
  exit 0
fi

if [ -z "$LANG_ARG" ]; then
  echo "Error: Please specify a language code or run with --all."
  echo ""
  usage
fi

lang="$LANG_ARG"

# Gather translated files
trans_files=$(find pages -type f \( -name "*.$lang.text" -o -name "*.$lang.md" -o -name "$lang.text" -o -name "$lang.md" \) | sort)
trans_count=$(echo "$trans_files" | grep -v '^$' | wc -l | tr -d ' ')

if [ "$MODE" != "untranslated" ]; then
  echo "Checking $trans_count $lang translation(s)..."
  outdated_found=0

  for file in $trans_files; do
    [ -z "$file" ] && continue
    # Derive the corresponding English original path
    orig=$(dirname "$file")/$(basename "$file" | sed -e "s/\.$lang\./.en./" -e "s/^$lang\./en./")

    if [ ! -f "$orig" ]; then
      continue
    fi

    # Native Git timestamps in seconds since epoch (portable, no GNU date needed)
    date_trans_s=$(git log -n 1 --format=%ct -- "$file" 2>/dev/null || echo 0)
    date_orig_s=$(git log -n 1 --format=%ct -- "$orig" 2>/dev/null || echo 0)

    if [ -n "$date_orig_s" ] && [ -n "$date_trans_s" ] && [ "$date_orig_s" -gt "$date_trans_s" ]; then
      outdated_found=$((outdated_found + 1))
      date_trans_human=$(git log -n 1 --format="%cd (%cr)" --date=short -- "$file" 2>/dev/null)
      date_orig_human=$(git log -n 1 --format="%cd (%cr)" --date=short -- "$orig" 2>/dev/null)
      
      echo ""
      echo "------------------------------------------------------------------------"
      echo "[OUTDATED] $file"
      echo "  Last translation: $date_trans_human"
      echo "  English modified: $date_orig_human ($orig)"
      
      # Find earliest commit to original since the translation
      commit=$(git log --pretty='%H' --reverse --since="$date_trans_s" -- "$orig" | head -n 1)
      if [ -n "$commit" ]; then
        echo "  Commit: $(git log -n 1 --oneline "$commit")"
      fi

      if [ "$MODE" = "diff" ] && [ -n "$commit" ]; then
        echo ""
        git --no-pager diff "${commit}^..HEAD" -- "$orig" || true
      elif [ "$MODE" = "difftool" ] && [ -n "$commit" ]; then
        git difftool "$commit" -- "$orig"
      fi
    fi
  done

  echo ""
  if [ "$outdated_found" -eq 0 ]; then
    echo "All $trans_count existing $lang translation(s) are up to date with English!"
  else
    echo "Found $outdated_found outdated $lang translation(s)."
  fi
fi

if [ "$MODE" != "outdated" ]; then
  echo ""
  echo "Checking for untranslated pages..."
  missing_found=0
  for orig in $(find pages -type f \( -name "*.en.text" -o -name "*.en.md" -o -name "en.text" -o -name "en.md" \) | sort); do
    translation=$(dirname "$orig")/$(basename "$orig" | sed -e "s/\.en\./.$lang./" -e "s/^en\./$lang./")
    if [ ! -f "$translation" ]; then
      missing_found=$((missing_found + 1))
      if [ "$MODE" = "untranslated" ]; then
        echo " - $orig"
      fi
    fi
  done

  if [ "$MODE" != "untranslated" ]; then
    echo "Found $missing_found page(s) missing a $lang translation."
    echo "(Run with '--untranslated-only $lang' to view the full list)"
  else
    echo ""
    echo "Total missing $lang translations: $missing_found"
  fi
fi

echo ""
echo "Done. Happy hacking!"

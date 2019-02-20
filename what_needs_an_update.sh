#!/bin/bash
# We are looking for translated files that have been translated prior to the last change to the original.
# Then we show the diff for the original file since the last commit to the translation.
# Limitation: It might be necessary to check more than the last commit for translated files.
if [ ! -d pages ] ; then echo "Are we in the correct directory? Missing 'pages'."; exit 1; fi
# select a language
if [ -z $1 ] ; then echo "Which language?
    zh: Simplified Chinese
    es: Spanish
    en: English
    pt: Portuguese
    ru: Russian
    de: German
    fr: French
    it: Italian
    el: Greek
    ca: Catalan"; exit 1; fi
lang=$1
debug=0
function debug {
  [ 0 -lt $debug ] && echo -e "\t$@"
}

# We want to print the last change for each original file,
# let's collect all translations first.
count=$(find pages |grep -e $lang.text -e $lang.md|wc -l)
echo "Checking $count $lang translations .."
for file in $(find pages |grep -e $lang.text -e $lang.md)
do
  echo -ne "\r$file"
  # get date of last commit to $file
  # get last commit: $git rev-list --all -1 -- $file
  date_s=$(date +%s -d "$(git log -n 1 --date=iso $file|grep Date|cut -f2 -d':')")
  date=$(date -d @$date_s)
  debug "$file: $date [$date_s]"
  # find english original
  orig=$(dirname  $file)/$(basename $file|sed -r "s/\.$lang\./\.en\./")
  # get date of last commit to english file
  date_en_s=$(date +%s -d "$(git log -n 1 --date=iso $orig|grep Date|cut -f2 -d':')")
  date_en=$(date -d @$date_en_s)
  debug "$orig: $date_en [$date_en_s]"
  # skip those where translation was changed last
  if [ $date_en_s -gt $date_s ]
  then
    # print commits to english file since last change to translation
    commit=$(git log --pretty='%H' --reverse --since "$date_s" -- $orig|head -n1)
    echo -e "\rShowing changes to $orig since $date"
    git log -n1 $commit
    git difftool $commit -- $orig
  else debug "$file is current."
  fi
done

echo -e "\r
Now let's look for untranslated files:"
for file in $(find pages |grep -e en.text -e en.md)
do
translation=$(dirname  $file)/$(basename $file|sed -r "s/en\./$lang\./")
[ -f $translation ] && echo -n "." || echo -e "\r - $file"
done
echo -e "\rDone. Happy hacking!"

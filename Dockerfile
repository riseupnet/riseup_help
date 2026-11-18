FROM ruby:2.7-bullseye

# Install system dependencies required for compiling amber and native gems
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install bundler and gem dependencies
COPY Gemfile ./
RUN gem install bundler:2.4.22 && bundle install

# Copy repository source code
COPY . .

# Expose amber server preview port
EXPOSE 8000

# Default command: launch amber preview server
CMD ["bundle", "exec", "amber", "server"]

# Base Image
FROM docker.io/fedora:40

# Install packages + Node + dependencies for atuin
RUN dnf update -y && \
    dnf install -y curl git which zsh pnpm nodejs22 fish sqlite sqlite-devel && \
    dnf clean all

# Create a new user
RUN useradd -m -s /bin/fish dev

# Switch to the new user
USER dev

# Install atuin
RUN curl --proto '=https' --tlsv1.2 -LsSf https://setup.atuin.sh | sh

# Set the working directory
WORKDIR /app

# Create atuin.sh script with initialization for fish
RUN mkdir -p ~/.config/fish && \
    echo 'atuin init fish | source' > ~/.config/fish/config.fish

# Copy package.json and package-lock.json to the working directory
COPY --chown=dev:dev package.json package-lock.json ./

# Install Node.js dependencies
RUN npm ci

# Expose the port for the Vite development server
EXPOSE 5173

# Start the Vite server and bind it to 0.0.0.0
CMD ["npm", "run", "dev", "--", "--host=0.0.0.0"]

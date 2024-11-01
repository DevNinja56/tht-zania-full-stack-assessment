# Stage 1: Build the React application
FROM node:18-alpine AS build

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the React application
RUN npm run build

# Stage 2: Run the React application
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy the build files from the previous stage
COPY --from=build /app/build ./build

# Install a minimal set of dependencies for serving
COPY package*.json ./
RUN npm install -g serve

# Expose the port on which the app will run
EXPOSE 3000

# Command to serve the React app on port 3000
CMD ["serve", "-s", "build", "-l", "3000"]

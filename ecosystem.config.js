const path = require("path");

const py = path.join(__dirname, ".venv", "bin", "python");

module.exports = {
  apps: [
    {
      name: "agent",
      script: "scripts/loop.py",
      interpreter: py,
      cwd: __dirname,
      env_file: ".env",
    },
    {
      name: "dashboard",
      script: "scripts/dashboard.py",
      interpreter: py,
      cwd: __dirname,
      env_file: ".env",
    },
  ],
};

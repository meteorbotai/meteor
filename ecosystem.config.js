module.exports = {
  apps: [
    {
      name: "agent",
      script: "scripts/loop.py",
      interpreter: ".venv/bin/python",
      cwd: __dirname,
      env_file: ".env",
    },
  ],
};

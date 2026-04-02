module.exports = {
  apps: [
    {
      name: "agent",
      script: "loop.py",
      interpreter: ".venv/bin/python",
      cwd: __dirname,
    },
  ],
};

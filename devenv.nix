{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/services/
  # services.postgres.enable = true;

  packages = [
    pkgs.pyright
    pkgs.sqlite
  ];

  languages.python = { 
    enable = true; 
    directory = "./tool";
    venv = {
      enable = true;
      requirements = ./tool/requirements.txt;
    };
  };

  # https://devenv.sh/pre-commit-hooks/
  # pre-commit.hooks.shellcheck.enable = true;

  # https://devenv.sh/processes/
  # processes.ping.exec = "ping example.com";

  # See full reference at https://devenv.sh/reference/options/
}

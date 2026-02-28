# Tiny Projects

Small independent projects, for learning purposes.

## Getting Started

Make sure you have nix installed, or install it [here](https://nixos.org/download).

```sh
nix run github:aintnodev/poytoy -- run project_path
```

> [!IMPORTANT]
> Other available options are `sync` and `build` to install dependencies and build project, though all projects don't ship with all options. To see available options, see options column in table below.

## Available Projects

If you don't wanna use nix, you can build manually. Look at project's poytoy.toml.

| Name         | Dependencies | Options |
| ------------ | ------------ | ------- |
| Base 64      | `uv`         | `run`   |
| Game of Life | `uv`         | `run`   |

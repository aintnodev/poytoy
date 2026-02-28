{
  description = "Teeny tiny projects";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in
    {
      packages.${system}.default = pkgs.stdenv.mkDerivation {
        pname = "poytoy";
        version = "0.1.0";
        src = ./poytoy;

        buildInputs = [ pkgs.makeWrapper ];

        installPhase = ''
          mkdir -p $out/bin
          cp $src/poytoy.py $out/bin/poytoy
          chmod +x $out/bin/poytoy

          wrapProgram $out/bin/poytoy --prefix PATH:${
            pkgs.lib.makeBinPath [
              pkgs.python3
              pkgs.uv
            ]
          }
        '';
      };
    };
}

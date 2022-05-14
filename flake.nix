{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
    let 
      pkgs = nixpkgs.legacyPackages.${system}; 
    in
    {
      devShell = pkgs.mkShell 
      {
        buildInputs = with pkgs; [
          python39
          python39Packages.flask
          python39Packages.gunicorn
          python39Packages.pyyaml
          python39Packages.urllib3
        ];
      };
    });
}

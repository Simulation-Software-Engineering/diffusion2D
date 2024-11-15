# shell.nix
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.stdenv.cc.cc  # GCC and related C libraries
    pkgs.python312Packages.pip
    pkgs.glib
    pkgs.zlib
    pkgs.libGL
    pkgs.fontconfig
    pkgs.xorg.libX11
    pkgs.libxkbcommon
    pkgs.freetype
    pkgs.dbus
  ];

  shellHook = ''
    # Set the LD_LIBRARY_PATH to include the necessary libraries from GCC
    export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [
      pkgs.stdenv.cc.cc
      pkgs.libz
    ]}
   echo "LD_LIBRARY_PATH has been set to include GCC libraries."
  '';
}

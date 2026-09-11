#!/bin/bash

set -e

echo "Generando archivos Markdown de la Wiki..."

for archivo in wiki/*.qmd; do
    quarto render "$archivo" --to gfm
done

echo "Sincronizando con el repositorio de la Wiki..."

WIKI_REPO="../Git-Wreckers.wiki"

if [ ! -d "$WIKI_REPO" ]; then
    echo "Error: no se encontró $WIKI_REPO"
    exit 1
fi

cp wiki/*.md "$WIKI_REPO/"

echo "Wiki generada y sincronizada correctamente."


#!/bin/bash

# La línea que quieres añadir al final del .bashrc
PS1_line="PS1='\[\033[0;34m\]\u@\h:\w\$' \[\033[0m\]'"

# Ruta al archivo .bashrc
bashrc_path="$HOME/.bashrc"

# Añade la línea al final del archivo .bashrc si no está ya presente
if ! grep -qF "$PS1_line" "$bashrc_path"; then
    echo -e "\n# Añadido por script\n$PS1_line" >> "$bashrc_path"
    echo "Línea añadida con éxito al archivo .bashrc."
else
    echo "La línea ya existe en el archivo .bashrc. No se hizo ningún cambio."
fi

#!/usr/bin/env bash
#renkuize_packrat.sh

# Error
err() {
  echo "Error: $@" >&2
  exit 1
}

# Main
# (1) proj_dir  project directory path
main() {

  local proj_dir
  proj_dir="${1}"
  [[ ! -d "${proj_dir}" ]] && err "Directory not found: ${proj_dir}"

  local packrat_dir
  packrat_dir=/home/rstudio/packrat
  [[ ! -d "${packrat_dir}" ]] && err "Directory not found: ${packrat_dir}"

  local libs
  libs=($(ls -d "${packrat_dir}"/lib*))
  for l in "${libs[@]}"; do
    rm -r "${proj_dir}"/packrat/$(basename "${l}") && \
    echo "Removed ${proj_dir}/packrat/$(basename ${l})"
    ln -s "${l}" "${proj_dir}"/packrat/$(basename "${l}") && \
    echo "Created symlink ${proj_dir}/packrat/$(basename ${l})->${l}"
  done

  return 0
}

main "${@}"

exit 0

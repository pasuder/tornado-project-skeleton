#!/bin/bash

export __dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export __dir="$( dirname ${__dir} )"

if [ -z "${1}" ]
then
    echo -n "Name: "
    read name
else
    name=${1}
fi

if [ -z "${name}" ]
then
    echo "No name provided"
    exit 1
fi

set -x

mv ${__dir}/src/python_project_skeleton/ ${__dir}/src/${name//-/_}
sed -i "s/tornado_project_skeleton/${name//-/_}/g" ${__dir}/src/${name//-/_}/main.py
sed -i "s/tornado_project_skeleton/${name//-/_}/g" ${__dir}/setup.py
sed -i "s/tornado_project_skeleton/${name//-/_}/g" ${__dir}/MANIFEST.in
sed -i "s/tornado_project_skeleton/${name//-/_}/g" ${__dir}/bin/main.sh

sed -i "s/tornado-project-skeleton/${name//_/-}/g" ${__dir}/README.md
sed -i "s/tornado-project-skeleton/${name//_/-}/g" ${__dir}/setup.py

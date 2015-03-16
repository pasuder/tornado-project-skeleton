#!/bin/bash

export __dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export __dir="$( dirname ${__dir} )"

if [ -z "${1}" ]
then
    echo -n "Name: "
    input name
else
    name=${1}
fi

if [ -z "${name}" ]
then
    echo "No name provided"
    exit 1
fi

set -x

mv ${__dir}/src/python_project_skeleton/ ${__dir}/src/${name}
sed -i "s/python_project_skeleton/${name}/g" ${__dir}/src/${name}/main.py
sed -i "s/python_project_skeleton/${name}/g" ${__dir}/setup.py
sed -i "s/python_project_skeleton/${name}/g" ${__dir}/MANIFEST.in
sed -i "s/python_project_skeleton/${name}/g" ${__dir}/README.md
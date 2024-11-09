# set -x

pushd $(pwd)
SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

cd ${SCRIPTPATH}
cd docs
make clean
cd ..
sphinx-autobuild docs/source/ docs/build/html/

popd

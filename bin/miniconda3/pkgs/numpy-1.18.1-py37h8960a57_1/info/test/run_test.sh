

set -ex



f2py -h
export OPENBLAS_NUM_THREADS=1
pytest --verbose --pyargs numpy -k "not (_not_a_real_test or test_sincos_float32)" --durations=0
exit 0
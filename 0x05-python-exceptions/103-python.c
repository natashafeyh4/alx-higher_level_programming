#include <Python.h>

/**
 * print_python_list - Print Python list info
 * @p: PyObject pointer
 */
void print_python_list(PyObject *p) {
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size, allocated, i;
    PyObject *item;

    if (PyList_Check(p)) {
        size = Py_SIZE(p);
        allocated = list->allocated;
        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", allocated);

        for (i = 0; i < size; i++) {
            item = PyList_GET_ITEM(list, i);
            printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        }
    } else {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
    }
}

/**
 * print_python_bytes - Print Python bytes info
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size, i;
    char *string;

    if (PyBytes_Check(p)) {
        size = Py_SIZE(p);
        string = bytes->ob_sval;

        printf("[.] bytes object info\n");
        printf("  size: %ld\n", size);
        printf("  trying string: %s\n", string);

        if (size <= 10) {
            printf("  first %ld bytes:", size);
            for (i = 0; i < size; i++) {
                printf(" %02x", string[i] & 0xFF);
            }
            printf("\n");
        } else {
            printf("  first 10 bytes:");
            for (i = 0; i < 10; i++) {
                printf(" %02x", string[i] & 0xFF);
            }
            printf("\n");
        }
    } else {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
    }
}

/**
 * print_python_float - Print Python float info
 * @p: PyObject pointer
 */
void print_python_float(PyObject *p) {
    PyFloatObject *floatObj = (PyFloatObject *)p;

    if (PyFloat_Check(p)) {
        double value = floatObj->ob_fval;
        printf("[.] float object info\n");
        printf("  value: %f\n", value);
    } else {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
    }
}

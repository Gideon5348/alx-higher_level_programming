#define PY_SSIZE_T_CLEAN
#include "Python.h"

/**
 * print_python_string - Print information about a Python string object
 * @p: Pointer to a PyObject representing a Python string object
 */
void print_python_string(PyObject *p)
{
    if (PyUnicode_Check(p))
    {
        Py_ssize_t length = PyUnicode_GET_LENGTH(p);
        Py_UCS4 *value = PyUnicode_AsUCS4String(p);
        if (value)
        {
            printf("[.] string object info\n");
            printf("  type: %s\n", Py_TYPE(p)->tp_name);
            printf("  length: %ld\n", length);
            printf("  value: ");
            for (Py_ssize_t i = 0; i < length; ++i)
            {
                if (PyUnicode_IS_COMPACT_ASCII(p) && Py_ISASCII(value[i]))
                    printf("%c", (char)value[i]);
                else
                    printf("\\u%04lx", (unsigned long)value[i]);
            }
            printf("\n");
            PyMem_Free(value);
            return;
        }
    }
    fprintf(stderr, "[.] string object info\n");
    fprintf(stderr, "  [ERROR] Invalid String Object\n");
}

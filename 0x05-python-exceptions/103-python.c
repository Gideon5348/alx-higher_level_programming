#include <Python.h>
#include <float.h>

/**
 * print_python_list - Prints information about a Python list object.
 * @p: The PyObject representing the Python list.
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}


/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: The PyObject representing the Python bytes object.
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %ld bytes:", (size > 10) ? 10 : size);
	for (i = 0; i < ((size > 10) ? 10 : size); i++)
	{
		printf(" %02x", str[i] & 0xFF);
	}
	printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object.
 * @p: The PyObject representing the Python float object.
 */

void print_python_float(PyObject *p)
{
	double value;

	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	value = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  value: %.*g\n", DBL_DIG, value);
}

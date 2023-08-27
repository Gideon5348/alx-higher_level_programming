#include <Python.h>
#include <stdio.h>
#include <wchar.h>

/**
 * print_python_bytes - Print basic info about Python bytes objects.
 * @p: A pointer to a PyObject (assumed to be a PyBytesObject).
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size = PyBytes_GET_SIZE(p);
	unsigned char *raw_data = (unsigned char *)PyBytes_AS_STRING(p);

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(bytes))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", raw_data);

	printf("  first 10 bytes:");
	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		printf(" %02x", raw_data[i]);
	}
	printf("\n");
}

/**
 * print_python_list - Print basic info about Python lists.
 * @p: A pointer to a PyObject (assumed to be a PyListObject).
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_GET_SIZE(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = list->ob_item[i];
		const char *type_name = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, type_name);

		if (PyBytes_Check(item))
		{
			print_python_bytes(item);
		}
	}
}

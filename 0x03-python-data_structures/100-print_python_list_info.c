#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: PyObject pointer to the Python list
 */
 
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyListObject *list;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

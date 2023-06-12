#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, idx;
	PyObject *element;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	idx = 0; 
	while (idx < size)
	{
		printf("Element %d: ", idx);

		element = PyList_GetItem(p, idx);
		printf("%s\n", Py_TYPE(element)->tp_name);
		idx++;
	}
}

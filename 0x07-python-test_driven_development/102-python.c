#include "Python.h"

/**
 * print_python_string - function that prints Python strings
 *
 * @p: a pointer to a PyObject string object.
 */

void print_python_string(PyObject *p)
{
	long int len; /* store the length of the string object p */

	fflush(stdout);

	/* Check if the object type is a string */
	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	len = ((PyASCIIObject *)(p))->len;

	/* Check if the string is a compact ASCII string */
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", len);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &len));
}

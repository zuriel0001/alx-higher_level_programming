#include "lists.h"

/**
* print_dlistint - function that return all the elements of a dlistint_t list
*
* @h: pointer to the head of list
*
* Return: number of nodes.
*/

size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *node;
	size_t node_cont = 0;

	node = h;
	while (node)
	{
		node_cont++;
		node = node->next;
	}

	return (node_cont);
}

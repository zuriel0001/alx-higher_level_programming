#include "lists.h"

/**
 * check_cycle - a function that checks for a cycle in a linked list
 *
 * @list: linked list to be checked
 *
 * Return: 1 cycle exist, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (!list || !list->next)
		return (0);

	slow = list;
	fast = list;
	for (; slow && fast && fast->next;)
	/*while (slow && fast && fast->next)*/
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}

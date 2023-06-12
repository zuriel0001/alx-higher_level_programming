#include "lists.h"
#include <stddef.h>

listint_t *reverse_list(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_list - functuon to reverses a singly-linked list
 *
 * @head: pointer to first  node of the list to be reversed
 *
 * Return: pointer to the  head of reversed list.
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *new_node = *head;
	listint_t *next_node, *prev = NULL;

	while (new_node)
	{
		next_node = new_node->next;
		new_node->next = prev;
		prev = new_node;
		new_node = next_node;
	}

	*head = prev;
	return (*head);
}


/**
 * is_palindrome: a function that checks for palindrome
 *
 * @head: point to first node of linked list
 *
 * Return: 0 if it is not else 1 if its a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *any_node, *rev, *mid;
	size_t size = 0, idx;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	any_node = *head;
	while (any_node)
	{
		size++;
		any_node = any_node->next;
	}

	any_node = *head;
	idx = 0; 
	while (idx < (size / 2) - 1)
	{
		any_node = any_node->next;
		idx++;
	}
	if ((size % 2) == 0 && any_node->n != any_node->next->n)
		return (0);

	any_node = any_node->next->next;
	rev = reverse_list(&any_node);
	mid = rev;

	any_node = *head;
	for (; rev; rev = rev->next)
	{
		if (any_node->n != rev->n)
			return (0);
		any_node = any_node->next;
	}
	reverse_list(&mid);

	return (1);
}

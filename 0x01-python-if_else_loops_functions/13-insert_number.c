#include "lists.h"

/**
 * insert_node - a function thati nserts number into a sorted singly-linked list
 *
 * @head: a pointer to the head of the linked list structure
 * @number: number to be inserted
 *
 * Return: NULL on failure else a pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *any_node = *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (any_node == NULL || any_node->n >= number)
	{
		new_node->next = any_node;
		*head = new_node;
		return (new_node);
	}

	while (any_node && any_node->next && any_node->next->n < number)
		any_node = any_node->next;

	new_node->next = any_node->next;
	any_node->next = new_node;

	return (new_node);
}

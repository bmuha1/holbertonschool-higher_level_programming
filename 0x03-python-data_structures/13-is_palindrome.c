#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Check if a linked list is a palindrome
 * @head: The list
 *
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *a = *head;
	listint_t *b = NULL;
	int nodes = 0, i;

	(void) b;

	if (*head == NULL)
		return (1);

	while (a != NULL)
	{
		a = a->next;
		nodes++;
	}

	for (i = 0; i < nodes / 2; i++)
	{
		if (get_value_at(*head, i) !=
		    get_value_at(*head, nodes - i - 1))
			return (0);

	}

	return (1);
}

/**
 * get_value_at - Get the value of a node at a given index
 * @h: The list
 * @index: The index
 *
 * Return: The value at the index
 */
int get_value_at(listint_t *h, int index)
{
	while (index)
	{
		h = h->next;
		index--;
	}

	return (h->n);
}

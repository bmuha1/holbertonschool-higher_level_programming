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
	int i, nodes = 0;

	if (*head == NULL)
		return (1);

	b = malloc(sizeof(listint_t));
	if (!b)
		return (1);

	while (a)
	{
		add_nodeint(&b, a->n);
		a = a->next;
		nodes++;
	}

	a = *head;
	for (i = 0; i < nodes / 2; i++)
	{
		if (a->n != b->n)
			return (0);
		a = a->next;
		b = b->next;
	}

	return (1);
}

/**
 * add_nodeint - Add a new node at the beginning of a listint_t list
 * @head: The list
 * @n: The integer
 *
 * Return: The address of the new element, or NULL if it failed
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = n;
	new->next = *head;

	*head = new;

	return (new);
}

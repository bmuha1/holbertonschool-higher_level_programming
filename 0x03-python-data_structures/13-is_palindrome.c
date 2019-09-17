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

	if (*head == NULL)
		return (1);

	b = malloc(sizeof(listint_t));
	if (!b)
		return (1);

	while (a)
	{
		add_nodeint_end(&b, a->n);
		a = a->next;
	}
	reverse_list(&b);

	a = *head;
	while (b->next)
	{
		if (a->n != b->n)
			return (0);
		a = a->next;
		b = b->next;
	}

	return (1);
}

/**
 * reverse_list - Reverse a linked list
 * @head: The list
 *
 * Return: Pointer to the new head
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;
	return (*head);
}

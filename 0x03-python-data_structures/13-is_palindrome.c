#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tempo, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tempo = *head;
	while (tempo)
	{
		size++;
		tempo = tempo->next;
	}

	tempo = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tempo = tempo->next;

	if ((size % 2) == 0 && tempo->n != tempo->next->n)
		return (0);

	tempo = tempo->next->next;
	rev = reverse_listint(&tempo);
	mid = rev;

	tempo = *head;
	while (rev)
	{
		if (tempo->n != rev->n)
			return (0);
		tempo = tempo->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}

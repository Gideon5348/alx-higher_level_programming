#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *next = NULL;
	listint_t *second_half = NULL;
	int palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
	return 1;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	slow = slow->next;

	second_half = slow;
	prev->next = NULL;

	while (second_half != NULL)
	{
		next = second_half->next;
		second_half->next = prev;
		prev = second_half;
		second_half = next;
	}

	second_half = prev;
	while (*head != NULL && second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			palindrome = 0;
		break;
		}
	*head = (*head)->next;
	second_half = second_half->next;
	}

	return palindrome;
}

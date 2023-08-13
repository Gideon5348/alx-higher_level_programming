#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: Pointer to the head of the linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
 
int check_cycle(listint_t *list) 
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	while (tortoise != NULL && hare != NULL && hare->next != NULL) 
	{
		tortoise = tortoise->next;        /* Tortoise moves one step */
		hare = hare->next->next;          /* Hare moves two steps */

	if (tortoise == hare) 
	{
		return 1;   /* Cycle detected */
	}
	}

	return 0; /* No cycle */
}

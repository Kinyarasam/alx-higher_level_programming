#include "lists.h"

/**
 * check_cycle - checks if function has a cycle in it.
 * @list: pointer
 *
 * Return: 0 if no cycle
 * otherwise: 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *head, *current;

	if (!list)
		return (0);
	head = list;
	current = list->next;
	while (head && current && current->next)
	{
		if (head == current)
			return (1);
		head = head->next;
		current = (current->next)->next;
	}
	return (0);
}

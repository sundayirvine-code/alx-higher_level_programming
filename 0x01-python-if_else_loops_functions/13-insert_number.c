#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *new, *temp;
	if (head == NULL)
		return (NULL)

	ptr = *head;
	new = NULL;
	temp = NULL;

	/* insert at begining */
	if (number < ptr -> n)
	{
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);
		new -> n = number;
		new -> next = ptr;
		*head = new;
		return (new);
	}

	/* middle and end */
	while(ptr -> n < number && ptr -> next != NULL)
	{
		ptr = ptr -> next;
	}

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new -> n = number;
	temp = ptr -> next;
	ptr -> next = new;
	new -> next = temp;
	return (new);
}

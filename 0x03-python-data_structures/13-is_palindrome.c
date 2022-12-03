#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - function that checks for a pallindrome
 * @head: pointer to linked list
 *
 * Return: 1 if pallindrome otherwise 0
 */

int is_palindrome(listint_t **head)
{
	int number, beg, end, x;
	listint_t *beg_ptr, *end_ptr;
	number = beg = 0;
	beg_ptr = *head;

	/* empty list*/
	if (!*head)
		return (1);

	/* find number of nodes*/
	while(beg_ptr)
	{
		number++;
		beg_ptr = beg_ptr -> next;
	}

	beg_ptr = *head;
	end = number - 1;

	while(beg < end)
	{
		end_ptr= *head;
		x = 0;
		while(x < end)
		{
			end_ptr = end_ptr -> next;
			x++;
		}
		/* compare end and beg values */
		if (end_ptr -> n != beg_ptr -> n)
			return (0);
		/* move to next value*/
		beg_ptr = beg_ptr -> next;
		end--;
		beg++;
	}
	return (1);
}


#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to a pointer to the head of the list
 *
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    int values[10000];
    int i = 0, j = 0;
    listint_t *current = *head;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (current != NULL)
    {
        values[i] = current->n;
        i++;
        current = current->next;
    }

    i--;
    while (i > j)
    {
        if (values[i] != values[j])
            return (0);
        i--;
        j++;
    }
    return (1);
}

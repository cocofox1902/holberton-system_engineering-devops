#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - infinite while with a latence of a second
 *
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - create 5 process zombie
 *
 * @i: index
 * @PID_zombie: pid zombie file
 * Return: 0
 */

int main(void)
{
	int i;
	pid_t PID_zombie;

	for (i = 0; i < 5; i++)
	{
		PID_zombie = fork();
		if (PID_zombie == 0)
			exit(0);
		printf("Zombie process created, PID: %d\n", PID_zombie);
		sleep(1);
	}
	infinite_while();
	return (0);
}
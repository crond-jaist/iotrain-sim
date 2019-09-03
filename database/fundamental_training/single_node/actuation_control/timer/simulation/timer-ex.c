#include "contiki.h"
#include "sys/etimer.h"
#include <stdio.h>

#define SECONDS 3
/*-------------------------------------------------*/
PROCESS(timer_process, "timer process");
AUTOSTART_PROCESSES(&timer_process);
/*-------------------------------------------------*/
PROCESS_THREAD(timer_process, ev, data)
{
    PROCESS_BEGIN();
    static struct etimer et;
    while (1)
    {
        etimer_set(&et, CLOCK_SECOND * SECONDS);
        PROCESS_WAIT_EVENT();
        if (etimer_expired(&et))
        {
            printf("Timer expired\n");
            etimer_reset(&et);
        }
    }
    PROCESS_END();
}

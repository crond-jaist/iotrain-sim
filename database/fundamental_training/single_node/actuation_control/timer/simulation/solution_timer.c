#include "contiki.h"
#include "sys/etimer.h"
#include "dev/leds.h"
#include <stdio.h>

#define SECONDS 1
/*-------------------------------------------------*/
PROCESS(blink_process, "blink process");
AUTOSTART_PROCESSES(&blink_process);
/*-------------------------------------------------*/
PROCESS_THREAD(blink_process, ev, data)
{
    PROCESS_BEGIN();
    static struct etimer et;
    while (1)
    {
        etimer_set(&et, CLOCK_SECOND * SECONDS);
        PROCESS_WAIT_EVENT_UNTIL(etimer_expired(&et));
        leds_on(LEDS_BLUE);
        printf("Blue LED is ON\n"); 

        etimer_set(&et, CLOCK_SECOND * SECONDS);
        PROCESS_WAIT_EVENT_UNTIL(etimer_expired(&et));
        leds_off(LEDS_BLUE);
        printf("Blue LED is OFF\n");
    }
    PROCESS_END();
}

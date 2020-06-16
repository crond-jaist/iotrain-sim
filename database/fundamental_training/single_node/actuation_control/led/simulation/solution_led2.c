#include "contiki.h"
#include "dev/leds.h"
#include <stdio.h>
/*---------------------------------------------------------------------------*/
PROCESS(led_process, "LED process");
AUTOSTART_PROCESSES(&led_process);
/*---------------------------------------------------------------------------*/
PROCESS_THREAD(led_process, ev, data)
{
  PROCESS_BEGIN();
  leds_on(LEDS_ALL);
  printf("LED %u status is %u\n", LEDS_ALL, leds_get());
  PROCESS_END();
}
/*---------------------------------------------------------------------------*/

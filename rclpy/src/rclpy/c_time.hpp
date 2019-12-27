
#ifndef C_TIME_HPP
#define C_TIME_HPP

#include <unistd.h>
#include <sys/time.h>

static size_t c_time()
{
        struct timespec tp;
        clock_gettime(CLOCK_REALTIME, &tp);
        size_t t = tp.tv_nsec + tp.tv_sec * 1000000000;
        return t;
}

static void print_t(size_t t1, size_t t2, const char* str)
{
	assert(t2 > t1);
	size_t e = t2 - t1;
	double e_ms = e * 1E-6;
        printf("%s %f ms\n", str, e_ms);
}
#endif

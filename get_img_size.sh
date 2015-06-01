identify *.{jpg} |awk '{split($(NF-6), a, /x/); split($0, b, /[[]/); print a[1], b[1]}' | sort -n | head -1 | { read size file; echo "smaller width is $file with size $size"; }
identify *.{jpg} |awk '{split($(NF-6), a, /x/); split($0, b, /[[]/); print a[2], b[1]}' | sort -n | head -1 | { read size file; echo "smaller height is $file with size $size"; }
identify *.{jpg} |awk '{split($(NF-6), a, /x/); split($0, b, /[[]/); print a[1], b[1]}' | sort -n | tail -1 | { read size file; echo "bigger width is $file with size $size"; }
identify *.{jpg} |awk '{split($(NF-6), a, /x/); split($0, b, /[[]/); print a[2], b[1]}' | sort -n | tail -1 | { read size file; echo "bigger height is $file with size $size"; }

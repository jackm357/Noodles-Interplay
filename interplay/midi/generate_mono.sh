"BUNDLE_PATH=/home/david/PycharmProjects/Noodles-Interplay/mags/mono.mag
CONFIG='mono.mag'

melody_rnn_generate \
--config=${CONFIG} \
--bundle_file=${BUNDLE_PATH} \
--output_dir=/tmp/melody_rnn/generated \
--num_outputs=10 \
--num_steps=128 \
--primer_melody=\"[60]\""
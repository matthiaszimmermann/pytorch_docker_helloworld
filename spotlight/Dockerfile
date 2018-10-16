FROM anibali/pytorch:latest

LABEL maintainer="https://github.com/matthiaszimmermann"

# install spotlight recommendation library
# https://github.com/maciejkula/spotlight
RUN conda install -c maciejkula spotlight=0.1.5 \
 && conda clean -ya

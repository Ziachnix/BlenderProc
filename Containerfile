
FROM docker.io/library/ubuntu:24.04

# install system dependencies
ENV DEBIAN_FRONTEND="noninteractive"
RUN apt-get update \
  && apt-get install --yes --no-install-recommends \
  ca-certificates \
  python3-pip \
  libxrender1 \
  libxxf86vm1 \
  libxfixes3 \
  libxi6 \
  libxkbcommon0 \
  libsm6 \
  libgl1 \
  libwayland-cursor0 \
  libwayland-egl1 \
  libdecor-0-0 \
  libegl1 \
  libglib2.0-0 \
  libglvnd0 \
  libwayland-egl \
  libwayland-cursor0 && \
  python3 -m pip config set global.break-system-packages true \
  && rm -rf /var/lib/{apt,dpkg,cache,log}

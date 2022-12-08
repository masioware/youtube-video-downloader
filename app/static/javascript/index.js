async function load_video_info() {
  // html elements
  const url_input_element = document.getElementsByName("url")[0];
  const thumbnail_img_element = document.getElementsByName("thumbnail")[0];
  const title_label_element = document.getElementsByName("title")[0];
  const length_lb_element = document.getElementsByName("lb-length")[0];
  const resolution_lb_element = document.getElementsByName("lb-resolution")[0];
  const resolution_select_element = document.getElementsByName("resolution")[0];
  const btn_submit_element = document.getElementsByName("submit")[0];

  // api request
  const url = url_input_element.value;
  const response = await fetch(`/video_info?url=${url}`);
  const { title, thumbnail, resolutions, length } = await response.json();

  // set values
  title_label_element.innerText = title;
  title_label_element.hidden = false;

  thumbnail_img_element.src = thumbnail;
  thumbnail_img_element.hidden = false;

  video_length = parse_seconds_to_minutses_plus_seconds(length);

  length_lb_element.innerText = `Length: ${video_length.minutes}:${video_length.seconds}s | `;
  length_lb_element.hidden = false;

  resolution_lb_element.hidden = false;

  resolution_select_element.innerHTML = null;
  resolutions.forEach((resolution) => {
    const option = document.createElement("option");

    option.innerHTML = resolution;
    option.value = resolution;

    resolution_select_element.appendChild(option);
  });
  resolution_select_element.hidden = false;

  btn_submit_element.hidden = false;
}

function parse_seconds_to_minutses_plus_seconds(time) {
  const minutes = Math.floor(time / 60);
  const seconds = time - minutes * 60;

  return { minutes, seconds };
}

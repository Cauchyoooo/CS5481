import { Chart, registerables } from "chart.js";
import {
  topojson,
  ChoroplethController,
  GeoFeature,
  ProjectionScale,
  ColorScale,
} from "chartjs-chart-geo";
import { race_data } from "./data/race_data";

Chart.register(
  ChoroplethController,
  GeoFeature,
  ProjectionScale,
  ColorScale,
  ...registerables
);

const popdensity = {
  "New Jersey": 488.0,
  "Rhode Island": 387.35,
  Massachusetts: 312.68,
  Connecticut: 271.4,
  Maryland: 209.23,
  "New York": 155.18,
  Delaware: 154.87,
  Florida: 114.43,
  Ohio: 107.05,
  Pennsylvania: 105.8,
  Illinois: 86.27,
  California: 83.85,
  Hawaii: 72.83,
  Virginia: 69.03,
  Michigan: 67.55,
  Indiana: 65.46,
  "North Carolina": 63.8,
  Georgia: 54.59,
  Tennessee: 53.29,
  "New Hampshire": 53.2,
  "South Carolina": 51.45,
  Louisiana: 39.61,
  Kentucky: 39.28,
  Wisconsin: 38.13,
  Washington: 34.2,
  Alabama: 33.84,
  Missouri: 31.36,
  Texas: 30.75,
  "West Virginia": 29.0,
  Vermont: 25.41,
  Minnesota: 23.86,
  Mississippi: 23.42,
  Iowa: 20.22,
  Arkansas: 19.82,
  Oklahoma: 19.4,
  Arizona: 17.43,
  Colorado: 16.01,
  Maine: 15.95,
  Oregon: 13.76,
  Kansas: 12.69,
  Utah: 10.5,
  Nebraska: 8.6,
  Nevada: 7.03,
  Idaho: 6.04,
  "New Mexico": 5.79,
  "South Dakota": 3.84,
  "North Dakota": 3.59,
  Montana: 2.39,
  Wyoming: 1.96,
  Alaska: 0.42,
  // "District of Columbia": 4297, // 添加 DC 的人口密度
};
const gdpData = {
  California: 100038,
  Texas: 85110,
  "New York": 110781,
  Florida: 70557,
  Illinois: 87033,
  Pennsylvania: 75189,
  Ohio: 74739,
  Georgia: 73558,
  "New Jersey": 86847,
  "North Carolina": 71373,
  Washington: 103462,
  Massachusetts: 105884,
  Virginia: 81794,
  Michigan: 66198,
  Colorado: 89469,
  Tennessee: 74081,
  Maryland: 83565,
  Arizona: 68965,
  Indiana: 73047,
  Minnesota: 82885,
  Wisconsin: 70569,
  Missouri: 68623,
  Connecticut: 94876,
  Oregon: 75477,
  "South Carolina": 60550,
  Louisiana: 68507,
  Alabama: 59174,
  Kentucky: 61961,
  Utah: 80476,
  Oklahoma: 63390,
  Iowa: 78209,
  Nevada: 75585,
  Kansas: 78348,
  Arkansas: 57657,
  Nebraska: 91553,
  // "District of Columbia": 259938,
  Mississippi: 49911,
  "New Mexico": 62209,
  Idaho: 60980,
  "New Hampshire": 79929,
  Hawaii: 75946,
  "West Virginia": 56630,
  Delaware: 91207,
  Maine: 65785,
  "North Dakota": 95082,
  "Rhode Island": 71122,
  "South Dakota": 79412,
  Montana: 62753,
  Alaska: 92272,
  Wyoming: 86880,
  Vermont: 67006,
  "United States": 81630,
};

fetch("https://unpkg.com/us-atlas/states-10m.json")
  .then((r) => r.json())
  .then((us) => {
    const nation = topojson.feature(us, us.objects.nation).features[0];
    const states = topojson.feature(us, us.objects.states).features;

    const populationChart = new Chart(
      document.getElementById("canvas").getContext("2d"),
      {
        type: "choropleth",
        data: {
          labels: states.map((d) => d.properties.name),
          datasets: [
            {
              label: "States",
              outline: nation,
              data: states.map((d) => ({
                feature: d,
                value: popdensity[d.properties.name] ?? 0,
              })),
            },
            {
              label: "DC: 4297 ",
              data: [
                {
                  feature: {
                    type: "Feature",
                    geometry: {
                      type: "Point",
                      coordinates: [-77.0369, 38.9072], // DC 的地理坐标 (经度, 纬度)
                    },
                    properties: { name: "District of Columbia" },
                  },
                },
              ],
              pointRadius: 100, // 点的大小
              backgroundColor: "#195E8E", // 点的颜色
            },
          ],
        },
        options: {
          plugins: {
            legend: {
              display: true,
              position: "bottom",
            },
          },
          scales: {
            projection: {
              axis: "x",
              projection: "albersUsa",
            },
            color: {
              quantize: 20,
              axis: "x",
              domain: [0, 500], // 数据范围从 0 到 500
              interpolate: "oranges",
              legend: {
                position: "bottom-right",
                align: "bottom",
              },
            },
          },
        },
      }
    );

    const resChart = new Chart(
      document.getElementById("canvas-res").getContext("2d"),
      {
        type: "choropleth",
        data: {
          labels: states.map((d) => d.properties.name),
          datasets: [
            {
              label: "States",
              outline: nation,
              data: states.map((d) => {
                return {
                  feature: d,
                  value:
                    (race_data[d.properties.name]?.["race_data"]["pct_dem"] ??
                      0) <
                      (race_data[d.properties.name]?.["race_data"]["pct_rep"] ??
                        0) ===
                    true
                      ? 1
                      : 0,
                };
              }),
            },
          ],
        },
        options: {
          plugins: {
            legend: {
              labels: {
                borderWidth: 0, // Remove label border
                borderColor: "transparent", // Ensure no border color
                generateLabels: function (chart) {
                  return [
                    { text: "Democratic Party", fillStyle: "#0047AB" },
                    { text: "Republican Party", fillStyle: "#D22B2B" },
                  ];
                },
              },
            },
          },
          scales: {
            projection: {
              axis: "x",
              projection: "albersUsa",
            },
            color: {
              quantize: 2,
              axis: "x",
              domain: [0, 100], // 数据范围从 0 到 500
              interpolate: (v) => (v === 0 ? "#0047AB" : "#D22B2B"),
              legend: {
                position: "bottom-right",
                align: "bottom",
              },
            },
          },
        },
      }
    );
    const res2020Chart = new Chart(
      document.getElementById("canvas-election2020").getContext("2d"),
      {
        type: "choropleth",
        data: {
          labels: states.map((d) => d.properties.name),
          datasets: [
            {
              label: "States",
              outline: nation,
              data: states.map((d) => {
                return {
                  feature: d,
                  value:
                    (race_data[d.properties.name]?.["historic_data"]?.[
                      "pct_dem"
                    ] ?? 0) <
                      (race_data[d.properties.name]?.["historic_data"]?.[
                        "pct_rep"
                      ] ?? 0) ===
                    true
                      ? 1
                      : 0,
                };
              }),
            },
          ],
        },
        options: {
          plugins: {
            legend: {
              labels: {
                borderWidth: 0, // Remove label border
                borderColor: "transparent", // Ensure no border color
                generateLabels: function (chart) {
                  return [
                    { text: "Democratic Party", fillStyle: "#0047AB" },
                    { text: "Republican Party", fillStyle: "#D22B2B" },
                  ];
                },
              },
            },
          },
          scales: {
            projection: {
              axis: "x",
              projection: "albersUsa",
            },
            color: {
              quantize: 2,
              axis: "x",
              domain: [0, 100], // 数据范围从 0 到 500
              interpolate: (v) => (v === 0 ? "#0047AB" : "#D22B2B"),
              legend: {
                position: "bottom-right",
                align: "bottom",
              },
            },
          },
        },
      }
    );
    const repchangeChart = new Chart(
      document.getElementById("canvas-change-rep").getContext("2d"),
      {
        type: "choropleth",
        data: {
          labels: [...states.map((d) => d.properties.name), 1, 2],
          datasets: [
            {
              label: "States",
              outline: nation,
              data: states.map((d) => {
                console.log(
                  d.properties.name,
                  (race_data[d.properties.name]?.["race_data"]?.["pct_rep"] ??
                    0) -
                    (race_data[d.properties.name]?.["historic_data"]?.[
                      "pct_rep"
                    ] ?? 0)
                );
                return {
                  feature: d,
                  value:
                    (race_data[d.properties.name]?.["race_data"]?.["pct_rep"] ??
                      0) -
                    (race_data[d.properties.name]?.["historic_data"]?.[
                      "pct_rep"
                    ] ?? 0),
                };
              }),
            },
            {
              label: "States1",
              outline: nation,
              data: [{ value: -10 }],
            },
            {
              label: "States2",
              outline: nation,
              data: [{ value: 10 }],
            },
          ],
        },
        options: {
          plugins: {
            legend: {
              labels: {
                borderWidth: 0, // Remove label border
                borderColor: "transparent", // Ensure no border color
                generateLabels: function (chart) {
                  return [
                    { text: "Democratic Party", fillStyle: "#0047AB" },
                    { text: "Republican Party", fillStyle: "#D22B2B" },
                  ];
                },
              },
            },
          },
          scales: {
            projection: {
              axis: "x",
              projection: "albersUsa",
            },
            color: {
              quantize: 10,
              axis: "x",
              interpolate: "reds",
              legend: {
                position: "bottom-right",
                align: "bottom",
              },
            },
          },
        },
      }
    );
    const demchangeChart = new Chart(
      document.getElementById("canvas-change-dem").getContext("2d"),
      {
        type: "choropleth",
        data: {
          labels: [...states.map((d) => d.properties.name), 1, 2],
          datasets: [
            {
              label: "States",
              outline: nation,
              data: states.map((d) => {
                return {
                  feature: d,
                  value: Math.max(
                    0,
                    (race_data[d.properties.name]?.["race_data"]?.["pct_dem"] ??
                      0) -
                      (race_data[d.properties.name]?.["historic_data"]?.[
                        "pct_dem"
                      ] ?? 0)
                  ),
                };
              }),
            },
          ],
        },
        options: {
          plugins: {
            legend: {
              labels: {
                borderWidth: 0, // Remove label border
                borderColor: "transparent", // Ensure no border color
                generateLabels: function (chart) {
                  return [
                    { text: "Democratic Party", fillStyle: "#0047AB" },
                    { text: "Republican Party", fillStyle: "#D22B2B" },
                  ];
                },
              },
            },
          },
          scales: {
            projection: {
              axis: "x",
              projection: "albersUsa",
            },
            color: {
              quantize: 5,
              axis: "x",
              interpolate: "blues",
              legend: {
                position: "bottom-right",
                align: "bottom",
              },
            },
          },
        },
      }
    );
    const demChart = new Chart(
      document.getElementById("canvas-dem").getContext("2d"),
      {
        type: "choropleth",
        data: {
          labels: states.map((d) => d.properties.name),
          datasets: [
            {
              label: "States",
              outline: nation,
              data: states.map((d) => {
                return {
                  feature: d,
                  value: Number(
                    race_data[d.properties.name]?.["race_data"]["pct_dem"] ?? 0
                  ),
                };
              }),
            },
          ],
        },
        options: {
          plugins: {
            legend: {
              display: false,
              position: "bottom",
            },
          },
          scales: {
            projection: {
              axis: "x",
              projection: "albersUsa",
            },
            color: {
              quantize: 4,
              axis: "x",
              domain: [0, 100], // 数据范围从 0 到 500
              interpolate: "blues",
              legend: {
                position: "bottom-right",
                align: "bottom",
              },
            },
          },
        },
      }
    );
    const repChart = new Chart(
      document.getElementById("canvas-rep").getContext("2d"),
      {
        type: "choropleth",
        data: {
          labels: states.map((d) => d.properties.name),

          datasets: [
            {
              label: "States",
              outline: nation,
              data: states.map((d) => {
                return {
                  feature: d,
                  value: Number(
                    race_data[d.properties.name]?.["race_data"]["pct_rep"] ?? 0
                  ),
                };
              }),
            },
          ],
        },
        options: {
          plugins: {
            legend: {
              display: false,
              position: "bottom",
            },
          },
          scales: {
            projection: {
              axis: "x",
              projection: "albersUsa",
            },
            color: {
              quantize: 4,
              axis: "x",
              domain: [0, 100], // 数据范围从 0 到 500
              interpolate: "reds",
              legend: {
                position: "bottom-right",
                align: "bottom",
              },
            },
          },
        },
      }
    );
    const gdpChart = new Chart(
      document.getElementById("canvas-gdp").getContext("2d"),
      {
        type: "choropleth",
        data: {
          labels: states.map((d) => d.properties.name),
          datasets: [
            {
              label: "States",
              outline: nation,
              data: states.map((d) => ({
                feature: d,
                value: gdpData[d.properties.name] ?? 0,
              })),
            },
          ],
        },
        options: {
          plugins: {
            legend: {
              display: true,
              position: "bottom",
            },
          },
          scales: {
            projection: {
              axis: "x",
              projection: "albersUsa",
            },
            color: {
              quantize: 5,
              axis: "x",
              interpolate: "purples",
              legend: {
                position: "bottom-right",
                align: "bottom",
              },
            },
          },
        },
      }
    );
  });

const nodeCoordinates = [
    { latitude: 37.7749, longitude: -122.4194 },  // Example coordinates; replace with your actual node coordinates
    { latitude: 34.0522, longitude: -118.2437 },
    { latitude: 40.7128, longitude: -74.0060 },
    // Add more coordinates as needed
];

const fastestPath = [0, 1, 2]; // Replace with your actual fastest path

function createMap() {
    const mapContainer = document.getElementById('map');
    const deviceWidth = window.innerWidth;
    const deviceHeight = window.innerHeight * 0.7; // Adjust based on your desired height ratio

    mapContainer.style.width = `${deviceWidth}px`;
    mapContainer.style.height = `${deviceHeight}px`;

    for (let i = 0; i < nodeCoordinates.length; i++) {
        for (let j = i + 1; j < nodeCoordinates.length; j++) {
            const path = document.createElement('div');
            path.className = 'path';
            const startPoint = getPixelCoordinates(nodeCoordinates[i]);
            const endPoint = getPixelCoordinates(nodeCoordinates[j]);
            path.style.left = `${startPoint.x}px`;
            path.style.top = `${startPoint.y}px`;
            path.style.width = `${endPoint.x - startPoint.x}px`;
            path.style.height = `${endPoint.y - startPoint.y}px`;
            mapContainer.appendChild(path);
        }
    }

    for (let i = 1; i < fastestPath.length; i++) {
        const pathIndex = fastestPath[i - 1] * (nodeCoordinates.length - 1) + fastestPath[i] - 1;
        const pathElement = mapContainer.querySelectorAll('.path')[pathIndex];
        pathElement.classList.add('highlighted-path');
    }
}

function getPixelCoordinates(coordinates) {
    // Convert latitude and longitude to pixel coordinates (adjust the conversion as needed)
    const x = (coordinates.longitude + 180) * (deviceWidth / 360);
    const y = ((-1 * coordinates.latitude) + 90) * (deviceHeight / 180);
    return { x, y };
}

createMap();

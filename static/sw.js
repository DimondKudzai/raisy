self.addEventListener("install", event => {
    event.waitUntil(
        caches.open("RAISY-cache").then(cache => {
            return cache.addAll([
                "/",
                "/upload"
            ]);
        })
    );
});

self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});
import rclpy
from rclpy.node import Node

from warehouse_interfaces.msg import DeliveryStatus
from warehouse_interfaces.srv import LoadPackage


class WarehouseNode(Node):

    def __init__(self):
        super().__init__('warehouse_node')

        self.robot_id = 'robot_01'
        self.package_count = 0
        self.battery = 100.0
        self.state = DeliveryStatus.STATE_IDLE

        self.publisher = self.create_publisher(
            DeliveryStatus, 'delivery_status', 10)

        self.create_timer(1.0, self.status_callback)

        self.service = self.create_service(
            LoadPackage, 'load_package', self.load_package_callback)

        self.get_logger().info('Warehouse node started')

    def status_callback(self):
        msg = DeliveryStatus()

        msg.robot_id = self.robot_id
        msg.package_count = self.package_count
        msg.battery = self.battery
        msg.state = self.state

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Robot: {msg.robot_id}, '
            f'Packages: {msg.package_count}, '
            f'Battery: {msg.battery}%'
        )

    def load_package_callback(self, request, response):

        if request.weight <= 10.0 and self.package_count < 5:
            self.package_count += 1
            response.accepted = True
            response.message = 'Package loaded successfully'

        elif request.weight > 10.0:
            response.accepted = False
            response.message = 'Package weight exceeds 10 kg'

        else:
            response.accepted = False
            response.message = 'Maximum limit of 5 packages reached'

        response.total_packages = self.package_count

        self.get_logger().info(response.message)

        return response


def main(args=None):
    rclpy.init(args=args)

    node = WarehouseNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()